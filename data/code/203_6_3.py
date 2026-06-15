import sys
def compare_baskets(basket1, basket2):
    cost1 = sum(basket1.values())
    cost2 = sum(basket2.values())
    if cost1 >= cost2:
        return basket1
    else:
        return basket2
if __name__ == '__main__':
    basket_a = {"apple": 1.50, "banana": 0.75, "milk": 3.00}
    basket_b = {"orange": 2.50, "cheese": 5.00, "bread": 2.00}
    result = compare_baskets(basket_a, basket_b)
    print(result)