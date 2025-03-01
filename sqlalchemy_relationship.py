from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Mapped, declarative_base, relationship, sessionmaker
from sqlalchemy.testing.schema import mapped_column

engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/postgres")
Base = declarative_base()

session = sessionmaker(engine)()

class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    products: Mapped[list["Product"]] = relationship(back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category : Mapped['Category'] =  relationship(back_populates="products")


# Base.metadata.create_all(engine)
query = select(Product)

for product in list(session.execute(query).scalar()):
    print(product.category.name)

# echo "# Relationship" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Holboeva/Relationship.git
# git push -u origin main