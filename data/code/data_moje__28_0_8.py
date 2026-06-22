def _get_comparator():
    return lambda x, y: x - y

def sort_pair(a, b):
    comp = _get_comparator()
    order_key = 'asc' if comp(a, b) <= 0 else 'desc'
    mapping = {
        'asc': (a, b),
        'desc': (b, a)
    }
    return mapping[order_key]

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    result = sort_pair(val1, val2)
    print(result)