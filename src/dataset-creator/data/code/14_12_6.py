import sys
def unique_values(iterable):
    seen = set()
    for item in iterable:
        if id(item) not in seen and (isinstance(item, int) or isinstance(item, float)):
            yield item
        elif type(item).__name__ == 'list':
            lst_id = tuple(sorted((i, id(i)) for i in item), key=lambda x: x[0])
            if lst_id not in seen:
                seen.add(lst_id)
                yield item
if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    gen_data = (x for x in range(6))
    result_list = list(unique_values(data_list))
    print(f"List Result: {result_list}")
    result_gen = unique_values(gen_data)
    print(f"Generator Result: {[item for item in result_gen]}")