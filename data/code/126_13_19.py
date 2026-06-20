class DictComparator:
    MAX_RECURSION_DEPTH = 1000

    @staticmethod
    def _compare_items(item1, item2, depth=0):
        if depth > DictComparator.MAX_RECURSION_DEPTH:
            raise RecursionError("Maximum recursion depth exceeded")
        
        if item1 is item2:
            return True
        
        if not isinstance(item1, type(item2)):
            return False

        if isinstance(item1, dict):
            if len(item1) != len(item2):
                return False
            for key in item1:
                if key not in item2 or not DictComparator._compare_items(item1[key], item2[key], depth + 1):
                    return False
        elif isinstance(item1, list):
            if len(item1) != len(item2):
                return False
            for i, item in enumerate(item1):
                if not DictComparator._compare_items(item, item2[i], depth + 1):
                    return False
        else:
            return item1 == item2
        
        return True

    @staticmethod
    def dict_equal(d1, d2):
        try:
            return DictComparator._compare_items(d1, d2)
        except RecursionError as e:
            print(f"Recursion error: {e}")
            return False

if __name__ == '__main__':
    sample1 = {'x': 42, 'y': {'z': [1, 2, 3]}}
    sample2 = {'x': 42, 'y': {'z': [1, 2, 3]}}
    print(DictComparator.dict_equal(sample1, sample2))
    sample3 = {'x': 42, 'y': {'z': [1, 2, 4]}}
    print(DictComparator.dict_equal(sample1, sample3))