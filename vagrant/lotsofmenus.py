from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
restaurant1 = Restaurant(name="Sharma's Restaurant")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name="Veg Burger", description="Juicy grilled veggie patty with tomato mayo",
                     price="$1.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="$2.00", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken burger with tomato mayo",
                     price="$4.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake", description="4 pieces which are fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Sizzwaan Burger", description="Very much spicy burger with chineese taste",
                     price="$2.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Masala Dosa", description="Famous South Indian dish like big bread with fried potato and sambhar",
                     price="$1.00", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="MNB", description="An Ice-cream shake",
                     price="$1.00", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich", description="Grilled toast with Cheese and tomato",
                     price="$1.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Paneer Butter Masala", description="Solid Milky soft pieces with tomtato gravy on it",
                     price="$3.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Annapurna")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Samosa", description="Triangular fried piece with potatos and vegetables inside it",
                     price="$0.5", course="Appetizer", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Paneer Butter Masala", description="Solid Milky soft pieces with tomtato gravy on it",
                     price="$1.99", course="Entree", restaurant=restaurant2)
    

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Cauliflower", description="Spicy gravy of cauliflower with onions and tomato mixed",
                     price="$1.99", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Momos", description="Steamed dumplings made with vegetables, spices and meat.",
                     price="1.99", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Mushroom", description="Spicy mushrooms with tomato gravy",
                     price="$1.99", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Spicy Lady Fingers", description="Spicy gravy of lady finger with onions and tomato mixed",
                     price="$1.99", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(name="Shree Shyam Restaurant")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Spicy Cauliflower", description="Spicy gravy of cauliflower with onions and tomato mixed",
                     price="$0.99", course="Entree", restaurant=restaurant1)


session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Gulab Jamun", description="sweet balls dip inside ice-cream",
                     price="$1.00", course="Dessert", restaurant=restaurant1)


session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mushroom", description="Spicy mushrooms with tomato gravy",
                     price="$2.00", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Spicy Lady Fingers", description="Spicy gravy of lady finger with onions and tomato mixed",
                     price="$0.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veg Pizza", description="Juicy grilled veggie patty with tomato mayo",
                     price="$1.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(name="All Night Canteen")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Spicy Lady Fingers", description="Spicy gravy of lady finger with onions and tomato mixed",
                     price="$0.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom", description="Spicy mushrooms with tomato gravy",
                     price="$1.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Banana Shake", description="Banana fruit milk shake",
                     price="$1.00", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$3.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi", description="Potato mixed with spicy cauliflower",
                     price="$2.99", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo",
                     price="$1.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(name="Blue Moon")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Gulab Jamun", description="sweet balls dip inside ice-cream",
                     price="$7.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken Biryani with small pieces of chicken dip inside rice",
                     price="$3.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce, chilies,ginger & green onions",
                     price="$3.99", course="Appetizer", restaurant=restaurant1)


session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="MNB", description="An Ice-cream shake",
                     price="$1.00", course="Beverage", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Paneer Butter Masala", description="Solid Milky soft pieces with tomtato gravy on it",
                     price="$3.99", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(name="Vijay Restaurant")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya, garlic sauce, chilies,ginger & green onions",
                     price="$1.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Gulab Jamun", description="Sweet balls dip inside ice-cream",
                     price="$0.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Tandoori Chicken", description="Delicious fried chicken available with tomato gravy and Indian chutney.",
                     price="$2.00", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Spicy Cauliflower", description="Spicy gravy of cauliflower with onions and tomato mixed",
                     price="$0.99", course="Entree", restaurant=restaurant1)


session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Paneer Butter Masala", description="Solid Milky soft pieces with tomtato gravy on it",
                     price="$3.99", course="Entree", restaurant=restaurant1)
session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(name="Golden Dragon")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(name="Chicken Lolipop", description="8 pieces of chicken lolipops",
                     price="$2.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Spicy Cauliflower", description="Spicy gravy of cauliflower with onions and tomato mixed",
                     price="$0.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce, chilies, ginger & green onions",
                     price="$1.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Lady Fingers", description="Spicy gravy of lady finger with onions and tomato mixed",
                     price="$0.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Fried chicken with tomato gravy and Indian chutney",
                     price="$1.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo",
                     price="$1.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Paneer Butter Masala", description="Solid Milky soft pieces with tomtato gravy on it",
                     price="$3.99", course="Entree", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(name="Jack n Jill")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Spicy Lady Fingers", description="Spicy gravy of lady finger with onions and tomato mixed",
                     price="$0.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chapati", description="Circular wheat bread",
                     price="$0.2", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(name="VK Reddy")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Samosa", description="Triangular fried piece with potatos and vegetables inside it",
                     price="$0.5", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit

menuItem1 = MenuItem(name="Bread Roll", description="Potato filled inside bread",
                     price="$1.00", course="Apetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Kela Rubdee", description="Sweet milk product on small pieces of banana",
                     price="$1.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print "added menu items!"
