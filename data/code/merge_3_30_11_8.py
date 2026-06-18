class CustomString:
    """A custom string-like class providing additional manipulation methods."""

    def __init__(self, value=""):
        self._value = list(value)

    def swap_adjacent_pairs(self):
        """
        Swaps the characters of every adjacent pair within this instance.
        
        If the length is odd, the last character remains unchanged.
        Example: "abcd" -> "badc", "abcde" -> "bcade"
        """
        n = len(self._value)
        for i in range(0, n - 1, 2):
            self._value[i], self._value[i + 1] = self._value[i + 1], self._value[i]

    def __str__(self):
        return "".join(self._value)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    tests = [
        "abcdefgh",
        "abcde",
        "",
        "a",
        "!@#$%",
        "1234567890"
    ]

    for original in tests:
        instance = CustomString(original)
        print(f"Original: {original}")
        instance.swap_adjacent_pairs()
        print(f"After swap: {instance}\n")