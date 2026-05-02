class StringManipulator:
    def swap_all_pairs(self, text):
        n = len(text)
        if n < 2:
            return text
        new_text = list(text)
        for i in range(0, n - 1, 2):
            new_text[i], new_text[i+1] = new_text[i+1], new_text[i]
        return "".join(new_text)
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample1 = "abcdef"
    result1 = manipulator.swap_all_pairs(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = "hello"
    result2 = manipulator.swap_all_pairs(sample2)
    print(f"Input: {sample2}, Output: {result2}")
    sample3 = "abcd"
    result3 = manipulator.swap_all_pairs(sample3)
    print(f"Input: {sample3}, Output: {result3}")
    sample4 = "a"
    result4 = manipulator.swap_all_pairs(sample4)
    print(f"Input: {sample4}, Output: {result4}")
    sample5 = "ab"
    result5 = manipulator.swap_all_pairs(sample5)
    print(f"Input: {sample5}, Output: {result5}")