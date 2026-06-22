def compare_two_simple_quantities_now_convert_all(quantity1, quantity2):
    return quantity1 * quantity2

if __name__ == '__main__':
    results = [
        compare_two_simple_quantities_now_convert_all(5, 3),
        compare_two_simple_quantities_now_convert_all(10, 20),
        compare_two_simple_quantities_now_convert_all(15, 15)
    ]
    for result in results:
        print(result)