import copy
class DataFilter:
    def filter_list(self, data: list, criteria) -> list:
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        filtered = []
        for item in data:
            keep_flag = True
            if 'value' in criteria and item == criteria['value']:
                keep_flag = False
            if 'type_excluded' in criteria and isinstance(item, tuple(criteria['type_excluded'])):
                keep_flag = False
            if callable(criteria.get('predicate')):
                try:
                    if not criteria['predicate'](item):
                        keep_flag = False
                except Exception as e:
                    raise RuntimeError(f"Predicate execution failed for item {item}: {e}") from None
            if keep_flag:
                filtered.append(item)
        return filtered
    def filter_set(self, data: set, criteria) -> set:
        if not isinstance(data, set):
            raise TypeError("Input must be a set.")
        result = {item for item in data 
                 if self._check_exclusion(item, criteria)}
        return result
    def filter_tuple(self, data: tuple, criteria) -> tuple:
        if not isinstance(data, tuple):
            raise TypeError("Input must be a tuple.")
        filtered_list = []
        for item in data:
            if self._check_exclusion(item, criteria):
                filtered_list.append(item)
        return tuple(filtered_list)
    def filter_dict(self, data: dict, key_criteria=None, value_criteria=None) -> dict:
        if not isinstance(data, dict):
            raise TypeError("Input must be a dictionary.")
        result = {}
        all_excluded_keys = set()
        if key_criteria is None and value_criteria is None:
            return data
        for k, v in data.items():
            should_keep = True
            if isinstance(key_criteria, dict):
                try:
                    if self._matches_key(k, key_criteria):
                        should_keep = False
                except Exception as e:
                    raise RuntimeError(f"Key validation failed for {k}: {e}") from None
            elif isinstance(value_criteria, dict):
                try:
                    if self._matches_value(v, value_criteria):
                        should_keep = False
                except Exception as e:
                    raise RuntimeError(f"Value validation failed for {k}:{v}: {e}") from None
            elif isinstance(key_criteria, (list, set)) or callable(key_criteria):
                try:
                    if self._matches_key(k, key_criteria) or not should_keep:
                        continue
                except Exception as e:
                    raise RuntimeError(f"Key validation failed for {k}: {e}") from None
            elif isinstance(value_criteria, (list, set)) or callable(value_criteria):
                try:
                    if self._matches_value(v, value_criteria) and should_keep:
                        continue
                except Exception as e:
                    raise RuntimeError(f"Value validation failed for {k}:{v}: {e}") from None
            if should_keep:
                result[k] = v
        return result
    def _check_exclusion(self, item, criteria):
        if 'value' in criteria and item == criteria['value']:
            return False
        if 'type_to_remove' in criteria:
            if isinstance(item, tuple(criteria['type_to_remove'])):
                return False
        if callable(criteria.get('predicate')):
            try:
                if not criteria['predicate'](item):
                    return False
            except Exception as e:
                raise RuntimeError(f"Predicate execution failed for item {item}: {e}") from None
        return True
    def _matches_key(self, key, criterion_specifier) -> bool:
        if isinstance(criterion_specifier, (list, set)):
            return key in criterion_specifier
        elif 'value' in criterion_specifier:
            return key == criterion_specifier['value']
        elif callable(criterion_specifier):
            try:
                if not criterion_specifier(key):
                    return False
            except Exception as e:
                raise RuntimeError(f"Key predicate failed: {e}") from None
        return True
    def _matches_value(self, value, criterion_specifier) -> bool:
        if isinstance(criterion_specifier, (list, set)):
            return value in criterion_specifier
        elif 'value' in criterion_specifier:
            return value == criterion_specifier['value']
        elif callable(criterion_specifier):
            try:
                if not criterion_specifier(value):
                    return False
            except Exception as e:
                raise RuntimeError(f"Value predicate failed: {e}") from None
        return True
if __name__ == '__main__':
    sample_list = [1, 'a', 2.5, 'b', 3]
    criteria_dict = {'value': 'b'}
    filtered_result = DataFilter().filter_list(sample_list, criteria_dict)
    print(f"Filtered List: {filtered_result}")