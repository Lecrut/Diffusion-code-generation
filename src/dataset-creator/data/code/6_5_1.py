if __name__ == '__main__':
    numbers = [2, 3, 4, 5]
    cumulative_product = 1
    for number in numbers:
        cumulative_product *= number
    print(cumulative_product)