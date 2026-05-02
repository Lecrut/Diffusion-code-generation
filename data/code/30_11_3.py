class CustomString:
    def __init__(self, text):
        self.text = text
    def swap_adjacent_pairs(self):
        n = len(self.text)
        if n < 2:
            return
        new_text = []
        for i in range(0, n, 2):
            if i + 1 < n:
                new_text.append(self.text[i+1])
                new_text.append(self.text[i])
            else:
                new_text.append(self.text[i])
        self.text = "".join(new_text)
if __name__ == '__main__':
    s1 = CustomString("abcdef")
    print(f"Original: {s1.text}")
    s1.swap_adjacent_pairs()
    print(f"Swapped: {s1.text}")
    s2 = CustomString("abcd")
    print(f"Original: {s2.text}")
    s2.swap_adjacent_pairs()
    print(f"Swapped: {s2.text}")
    s3 = CustomString("abcde")
    print(f"Original: {s3.text}")
    s3.swap_adjacent_pairs()
    print(f"Swapped: {s3.text}")
    s4 = CustomString("a")
    print(f"Original: {s4.text}")
    s4.swap_adjacent_pairs()
    print(f"Swapped: {s4.text}")
    s5 = CustomString("")
    print(f"Original: {s5.text}")
    s5.swap_adjacent_pairs()
    print(f"Swapped: {s5.text}")
    s6 = CustomString("ab")
    print(f"Original: {s6.text}")
    s6.swap_adjacent_pairs()
    print(f"Swapped: {s6.text}")