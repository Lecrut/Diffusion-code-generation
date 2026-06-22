EDGE_FIRST = 0
EDGE_LAST = -1

def get_edge_elements(lst):
    if not lst:
        raise ValueError("List must be non-empty")
    return (lst[EDGE_FIRST], lst[EDGE_LAST])

class ListAnalyzer:
    _first_index = 0
    _last_index = -1

    @staticmethod
    def _validate_input(data):
        if not data:
            raise ValueError("Data cannot be empty")
        return data

    @staticmethod
    def get_edges(data):
        validated = ListAnalyzer._validate_input(data)
        return (validated[ListAnalyzer._first_index], validated[ListAnalyzer._last_index])

if __name__ == '__main__':
    sample_input = [100, 200, 300, 400, 500]
    result_tuple = get_edge_elements(sample_input)
    print(result_tuple)
    class_result = ListAnalyzer.get_edges(sample_input)
    print(class_result)