class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        chars = list(self.text)
        left, right = 0, len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return ''.join(chars)

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    reverser = StringReverser(sample_text)
    reversed_text = reverser.reverse()
    print(reversed_text)