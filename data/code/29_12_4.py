class StringReverser:
    def reverse(self, s: str) -> str:
        return s[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample1 = "hello"
    sample2 = "world"
    sample3 = "python"
    sample4 = ""
    sample5 = "aabbaa"
    print(f"Reversing '{sample1}': {reverser.reverse(sample1)}")
    print(f"Reversing '{sample2}': {reverser.reverse(sample2)}")
    print(f"Reversing '{sample3}': {reverser.reverse(sample3)}")
    print(f"Reversing '{sample4}': {reverser.reverse(sample4)}")
    print(f"Reversing '{sample5}': {reverser.reverse(sample5)}")