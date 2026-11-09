# 1. I use .get() for keys that may not exist, e.g. for optional fields such as a phone number or a tier that isn’t in a lookup table. This gives me a safe default value and means my programme will still run. I use [] for keys that must exist, e.g. compulsory fields. 
# I find a KeyError is helpful here as it will tell me immediately that there is an issue with the data. As a general rule of thumb, if a key isn’t expected to exist then use 
# .get(), if it would cause a bug then use [] 

# 2. Like pivot tables or SUMIF formulas in excel. But this means that for large data sets it is much more efficient. 
# As you are only looping once through the data, this means it will be fast even for millions of rows. Whereas excel would take a long time or would have too many rows. 
# Also it is replicable so if you get new data you can just run the same code again without having to create a new pivot table.
    





#  exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
 
#  exercise 2: Update and add 
customer["phone"] = "555-1234"
print(customer)
 
customer["tier"] = "platinum"
print(customer)
 
del customer["email"]
print(customer)
 
#  exercise 3: Safe lookup 
print(customer.get("email", "no email on file"))
 
try:
    print(customer["email"])
except KeyError as err:
    print(f"KeyError raised for key: {err}")
 
#  exercise 4: Iterate 
for key, value in customer.items():
    print(f"{key}: {value}")
 
# Iterating without .items():
# A plain `for x in customer` loops over the KEYS only, so you get just the
# field names. .items() gives (key, value) pairs, so you get both at once.
for key in customer:
    print(key)
 
#  exercise 5: Lookup table 
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
 
rate = tier_discounts.get(customer["tier"], 0)
purchase = 200
final_price = purchase * (1 - rate)
print(f"Tier: {customer['tier']} | Discount: {rate:.0%} | Final price: ${final_price:.2f}")
 
#  exercise 6: List of dicts 
customer1 = {"name": "Alice", "tier": "platinum"}
customer2 = {"name": "Bob", "tier": "silver"}
customer3 = {"name": "Carla", "tier": "bronze"}
customers = [customer1, customer2, customer3]
 
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} ({c['tier']}): ${discount_amount:.2f} discount on ${purchase}")
 
#  exercise 7: Nested catalog 
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")
 
#  exercise 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
 
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]
 
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
