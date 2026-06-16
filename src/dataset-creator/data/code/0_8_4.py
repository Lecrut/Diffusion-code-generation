import sys
def deep_equality(a: object, b: object) -> bool:
    if type(a) != type(b):
        return False
    try:
        iter(a)
        is_iterable = True
    except TypeError:
        is_iterable = False
    if not (isinstance(a, dict) or isinstance(b, dict)):
        if is_iterable:
            try:
                a_list = list(a)
                b_list = list(b)
                if len(a_list) != len(b_list):
                    return False
                return a_list == b_list
            except TypeError:
                pass
        return False
    else:
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a:
            if not deep_equality(a[key], b.get(key)):
                return False
        return True
def main():
    sample_a = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Java"],
        "address": {"city": "New York", "zip": "10001"},
        "metadata": [True, None]
    }
    sample_b = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Java"],
        "address": {"city": "New York", "zip": "10001"},
        "metadata": [True, None]
    }
    sample_c = {
        "name": "Bob",
        "age": 30,
        "skills": ["Python"],
        "address": {"city": "New York"}
    }
    print(deep_equality(sample_a, sample_b))                 
    if __name__ == '__main__':
        pass