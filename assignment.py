sales = {"tea": 3, "coffee": 5}
orders = {"coffee", "juice", "tea"}
available = set(sales)
missing = orders - available
sales["juice"] = 2
print(sorted(sales.items()), sorted(missing))
