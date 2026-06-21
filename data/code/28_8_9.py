OPERATIONS = {
    "less": lambda x, y: x < y,
    "greater": lambda x, y: x > y
}

def order_pair(first, second):
    if OPERATIONS["less"](first, second):
        return (first, second)
    return (second, first)

if __name__ == '__main__':
    val1 = 15
    val2 = 3
    print(order_pair(val1, val2))
    
    val3 = -5
    val4 = 10
    print(order_pair(val3, val4))
    
    val5 = 7
    val6 = 7
    print(order_pair(val5, val6))