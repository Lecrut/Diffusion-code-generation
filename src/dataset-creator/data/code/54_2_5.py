def find_middle_index(sequence):
    if not sequence:
        return None
    n = len(sequence)
    if n % 2 == 0:
        middle_index = n // 2
    else:
        middle_index = n // 2
    return middle_index
if __name__ == '__main__':
    even_seq = [0, 1, 2, 3]
    odd_seq = [0, 1, 2]
    empty_seq = []
    print(f"Even sequence {even_seq} -> Middle Index: {find_middle_index(even_seq)}")
    print(f"Odd sequence {odd_seq} -> Middle Index: {find_middle_index(odd_seq)}")
    print(f"Empty sequence {empty_seq} -> Middle Index: {find_middle_index(empty_seq)}")