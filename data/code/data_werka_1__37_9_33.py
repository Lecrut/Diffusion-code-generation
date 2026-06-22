class StringCombiner:
    def combine(self, str1, str2):
        combined_result = self._concatenate(str1, str2)
        return combined_result

    def _concatenate(self, str1, str2):
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    first_string = 'Good morning, '
    second_string = 'Earth!'
    result = combiner.combine(first_string, second_string)
    print(result)