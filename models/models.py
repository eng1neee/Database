from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

roles = Table(
    "Roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("Name", String, nullable=False),
    Column("Permissions", JSON),
)

users = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey("roles.id")),
)