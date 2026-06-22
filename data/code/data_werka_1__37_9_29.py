class StringCombiner:
    def combine(self, str1, str2):
        combined_string = self._concatenate(str1, str2)
        return combined_string

    def _concatenate(self, part1, part2):
        return part1 + part2

if __name__ == '__main__':
    combiner_instance = StringCombiner()
    first_part = 'foo'
    second_part = 'bar'
    result = combiner_instance.combine(first_part, second_part)
    print(result)