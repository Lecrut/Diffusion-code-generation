class ListAppender:
    @staticmethod
    def append_lists(list_a, list_b):
        list_a.extend(list_b)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    ListAppender.append_lists(sample_list_a, sample_list_b)
    print(f"Updated list A: {sample_list_a}")