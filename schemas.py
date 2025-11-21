"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Inquiry(BaseModel):
    """
    Inquiries from website contact form
    Collection name: "inquiry"
    """
    company_name: Optional[str] = Field(None, description="Company name")
    contact_name: str = Field(..., description="Contact person's name")
    email: EmailStr = Field(..., description="Contact email")
    phone: Optional[str] = Field(None, description="Phone or WhatsApp number")
    country: Optional[str] = Field(None, description="Country of origin/destination")
    inquiry_type: Optional[str] = Field(
        None, description="Type of inquiry: export, import, buy, sell, partnership"
    )
    products: Optional[List[str]] = Field(
        default=None, description="List of products of interest (fruits, vegetables, grains, spices, etc.)"
    )
    message: Optional[str] = Field(None, description="Additional details")
    preferred_port: Optional[str] = Field(None, description="Preferred port of shipment")
