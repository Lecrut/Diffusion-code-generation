class MinFinder:
    @staticmethod
    def find_min(sequence):
        if not sequence:
            return None
        minimum = sequence[0]
        for number in sequence:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    data = [15, 3, 8, 22, 1]
    min_value = MinFinder.find_min(data)
    print(min_value)