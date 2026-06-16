import sys
def count_atomic_values(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            total += count_atomic_values(item)
        return total
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6], {7: "8"}, ("a", ["b", {"c": [9]}])]
    sample_list = []
    def extract_values(obj):
        if isinstance(obj, (list, tuple)):
            for item in obj:
                extract_values(item)
        elif isinstance(obj, dict):
            for val in obj.values():
                extract_values(val)
        else:
            return [obj]
    flattened = []
    def collect_items(current_list):
        if not current_list:
            return
        item_type = type(current_list[0])
        temp_sample = [1, 2, {3: "4"}, ("5", ["6"])]
        result = []
        def traverse(obj):
            if isinstance(obj, (list, tuple)):
                for x in obj:
                    result.append(x)
                    traverse(x)
            elif isinstance(obj, dict):
                for v in obj.values():
                    result.append(v)
                    traverse(v)
            else:
                result.append(obj)
        temp_sample_copy = [1] + list(temp_sample[0])                                                      
        final_list = []
        def make_final(lst):
             for x in lst:
                 try:
                     m = type(x).__name__
                     if isinstance(x, (int, float)):
                         return [x]
                     elif isinstance(x, str):
                         return [x]
                     else:
                         pass                                                                   
                 except:
                     pass
        final_list = []
        def deep_count(obj):
            if not obj or (isinstance(obj, list) and len(obj)==0):
                return 0
            count = 1 if isinstance(obj, (int, float)) else 0                                 
            if isinstance(obj, str):
                 pass
            elif isinstance(obj, dict):
                for val in obj.values():
                    count += deep_count(val)
            elif isinstance(obj, list):
                for item in obj:
                    count += deep_count(item)
            return count
        test_input = [10, 20, {"a": ["b", {"c": [45]}]}, (67, 89)]
        total_count = deep_count(test_input)
        print(total_count)