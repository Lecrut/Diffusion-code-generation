class CustomString:
    def __init__(self, s):
        self.value = s
    def swap_adjacent_pairs(self):
        n = len(self.value)
        if n < 2:
            return
        new_value = []
        for i in range(0, n, 2):
            if i + 1 < n:
                new_value.append(self.value[i+1])
                new_value.append(self.value[i])
            else:
                new_value.append(self.value[i])
        self.value = "".join(new_value)
if __name__ == '__main__':
    s1 = "abcdef"
    cs1 = CustomString(s1)
    print(f"Original: {s1}")
    cs1.swap_adjacent_pairs()
    print(f"Swapped: {cs1.value}")
    s2 = "abcd"
    cs2 = CustomString(s2)
    print(f"Original: {s2}")
    cs2.swap_adjacent_pairs()
    print(f"Swapped: {cs2.value}")
    s3 = "abcde"
    cs3 = CustomString(s3)
    print(f"Original: {s3}")
    cs3.swap_adjacent_pairs()
    print(f"Swapped: {cs3.value}")
    s4 = "a"
    cs4 = CustomString(s4)
    print(f"Original: {s4}")
    cs4.swap_adjacent_pairs()
    print(f"Swapped: {cs4.value}")
    s5 = ""
    cs5 = CustomString(s5)
    print(f"Original: '{s5}'")
    cs5.swap_adjacent_pairs()
    print(f"Swapped: '{cs5.value}'")
    s6 = "ab"
    cs6 = CustomString(s6)
    print(f"Original: {s6}")
    cs6.swap_adjacent_pairs()
    print(f"Swapped: {cs6.value}")