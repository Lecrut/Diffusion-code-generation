from typing import List
def sort_numeric_list(numbers: List[float]) -> List[float]:
    return sorted(numbers)
if __name__ == '__main__':
    raw_data = [5, 234109876543210, -42, 0.5, 1e-10, 'not a number', 3]
    try:
        numeric_data = [float(x) if isinstance(x, (int, str)) else x 
                        for x in raw_data 
                        if not isinstance(x, complex)]
        sorted_result = sort_numeric_list(numeric_data)
        print("Sorted Numeric List:")
        for item in sorted_result:
            print(item)
    except ValueError as ve:
        print(f"Error during conversion or sorting due to non-numeric data: {ve}")