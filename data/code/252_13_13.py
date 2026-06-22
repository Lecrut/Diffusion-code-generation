def compare_two_simple_quantities_now_rank_samples(a, b):
    return (a > b) - (a < b)

if __name__ == '__main__':
    result1 = compare_two_simple_quantities_now_rank_samples(10.5, 5.2)
    print(result1)
    result2 = compare_two_simple_quantities_now_rank_samples(3, 7)
    print(result2)
    result3 = compare_two_simple_quantities_now_rank_samples(-1.0, -5.0)
    print(result3)