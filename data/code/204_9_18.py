class MedianCalculator:
    @staticmethod
    def find_middle_index(N):
        if N <= 0:
            return None
        middle_floor = (N - 1) // 2
        middle_ceil = N // 2
        return middle_floor, middle_ceil

if __name__ == '__main__':
    calculator = MedianCalculator()
    list_length_odd = 5
    floor_idx, ceil_idx = calculator.find_middle_index(list_length_odd)
    print(f"List Length: {list_length_odd}")
    print(f"Floor Index (N-1)/2: {floor_idx}")
    print(f"Ceiling Index N/2: {ceil_idx}")

    list_length_even = 6
    floor_idx, ceil_idx = calculator.find_middle_index(list_length_even)
    print(f"\nList Length: {list_length_even}")
    print(f"Floor Index (N-1)/2: {floor_idx}")
    print(f"Ceiling Index N/2: {ceil_idx}")