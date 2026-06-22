class SetOperations:
    def symmetric_difference(self, set1, set2):
        return set1.symmetric_difference(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    operations = SetOperations()
    result = operations.symmetric_difference(sample_set1, sample_set2)
    print(result)