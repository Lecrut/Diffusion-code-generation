import numpy as np
def analyze_oddness_properties(data):
    data_int = np.array([int(x) for x in data], dtype=np.int64)
    total_sum = np.sum(data_int)
    average_value = np.mean(data_int)
    is_odd_mask = data_int % 2 != 0
    count_odds = np.count_nonzero(is_odd_mask)
    total_elements = len(data_int)
    percentage_odds = (count_odds / total_elements * 100) if total_elements > 0 else 0.0
    is_all_even = np.all(~is_odd_mask)
    is_all_odd = np.all(is_odd_mask)
    return {
        'total_sum': int(total_sum),
        'average_value': float(average_value),
        'count_odds': int(count_odds),
        'percentage_odds': float(percentage_odds),
        'is_all_even': bool(is_all_even),
        'is_all_odd': bool(is_all_odd)
    }
def main():
    sample_data = [1, 2, -3, 4, 5, -6, 7, 0, 8, 9]
    result = analyze_oddness_properties(sample_data)
    print(f"Total Sum: {result['total_sum']}")
    print(f"Average Value: {result['average_value']:.2f}")
    print(f"Count of Odd Numbers: {result['count_odds']}")
    print(f"Percentage of Odds: {result['percentage_odds']:.1f}%")
    print(f"All Even? {result['is_all_even']}")
    print(f"All Odd? {result['is_all_odd']}")
if __name__ == '__main__':
    main()