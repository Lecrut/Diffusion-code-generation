class PatternRepeater:
    def __init__(self, base_list):
        self.base_list = base_list

    def repeat_pattern(self, target_length):
        return [self.base_list[i % len(self.base_list)] for i in range(target_length)]

if __name__ == '__main__':
    repeater = PatternRepeater(['a', 'b', 'c'])
    result = repeater.repeat_pattern(10)
    print(result)