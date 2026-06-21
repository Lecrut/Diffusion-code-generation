class NestedListModifier:

    @staticmethod
    def remove_at_path(nested_list, path):
        current = nested_list
        for key in path[:-1]:
            if isinstance(current[key], list):
                current = current[key]
            else:
                raise ValueError(f'Path does not lead to a list at {key}')
        if isinstance(current[path[-1]], list):
            del current[path[-1]]
        else:
            raise ValueError(f'Target is not a list at {path[-1]}')
if __name__ == '__main__':
    sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    path_to_remove = [1, 0]
    NestedListModifier.remove_at_path(sample_list, path_to_remove)
    print(sample_list)
    sample_list_2 = [['a', 'b'], ['c', 'd', 'e'], ['f', 'g']]
    path_to_remove_2 = [1, 2]
    NestedListModifier.remove_at_path(sample_list_2, path_to_remove_2)
    print(sample_list_2)
    sample_list_3 = [[10, 20], [30, 40]]
    path_to_remove_3 = [0]
    NestedListModifier.remove_at_path(sample_list_3, path_to_remove_3)
    print(sample_list_3)