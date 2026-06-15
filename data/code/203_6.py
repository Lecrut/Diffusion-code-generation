import sys
def compare_baskets(basket1, basket2):
    cost1 = sum(basket1.values())
    cost2 = sum(basket2.values())
    if cost1 > cost2:
        return basket1
    elif cost2 > cost1:
        return basket2
    else:
        return None
if __name__ == '__main__':
    basket_a = {"apple": 1.0, "banana": 0.5, "milk": 3.5}
    basket_b = {"orange": 2.0, "cheese": 5.0, "bread": 2.5}
    result = compare_baskets(basket_a, basket_b)
    if result:
        print(result)