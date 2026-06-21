class ChecklistMembership:
    @staticmethod
    def is_member(element, frozenset_obj):
        return element in frozenset_obj

if __name__ == '__main__':
    sample_set = frozenset([1, 2, 3, 4, 5])
    print(ChecklistMembership.is_member(3, sample_set))
    print(ChecklistMembership.is_member(6, sample_set))