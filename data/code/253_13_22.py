class ValueRanker:
    @staticmethod
    def find_the_middle_value_among_three_rank_samples(a, b, c):
        return sorted([a, b, c])[1]

if __name__ == '__main__':
    middle_value = ValueRanker.find_the_middle_value_among_three_rank_samples(3, 1, 2)
    print(middle_value)