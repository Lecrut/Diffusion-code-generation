from collections import defaultdict
from typing import Any, Callable, Tuple

def get_with_composite_key(data: defaultdict, key: Tuple, default_factory: Callable[[], Any]) -> Any:
    if key not in data:
        data[key] = default_factory()
    return data[key]

if __name__ == '__main__':
    sample_data = defaultdict(list)
    composite_key = ("user_1", "action_login")
    default_factory = lambda: ["timestamp_placeholder"]
    
    result = get_with_composite_key(sample_data, composite_key, default_factory)
    print(result)
    
    result_after_init = get_with_composite_key(sample_data, composite_key, default_factory)
    print(result_after_init)
    
    new_key = ("user_2", "action_logout")
    new_result = get_with_composite_key(sample_data, new_key, default_factory)
    print(new_result)