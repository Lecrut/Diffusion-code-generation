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
    basket_a = {
        "apple": 1.50,
        "banana": 0.75,
        "milk": 3.20
    }
    basket_b = {
        "orange": 1.25,
        "cheese": 5.00,
        "bread": 2.50
    }
    result = compare_baskets(basket_a, basket_b)
    if result:
        print(result)