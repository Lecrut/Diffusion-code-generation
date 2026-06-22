EDGE_FIRST = 0
EDGE_LAST = -1

def get_edge_elements(lst):
    if len(lst) == 0:
        raise ValueError("List must not be empty")
    return (lst[EDGE_FIRST], lst[EDGE_LAST])

if __name__ == '__main__':
    data = [100, 200, 300]
    print(get_edge_elements(data))