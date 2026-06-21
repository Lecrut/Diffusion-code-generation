class FloatSummator:
    def sum_elements(self, float_list):
        return sum(float_list)

if __name__ == '__main__':
    summator = FloatSummator()
    sample_values = [1.5, 2.5, 3.5]
    result = summator.sum_elements(sample_values)
    print(result)