class ListJoiner:
    def join_lists(self, list_one, list_two):
        return list_one + list_two

if __name__ == '__main__':
    joiner = ListJoiner()
    result1 = joiner.join_lists([1, 2, 3], [4, 5, 6])
    print(result1)
    result2 = joiner.join_lists(['apple', 'banana'], ['cherry', 'date'])
    print(result2)