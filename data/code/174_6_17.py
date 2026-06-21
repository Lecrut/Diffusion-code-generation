def are_dicts_equal(dict1, dict2):
    return set(dict1.items()) == set(dict2.items())
if __name__ == '__main__':
    sample_dict1 = {'theme': 'dark', 'font_size': 12, 'notifications_enabled': True, 'language': 'en'}
    sample_dict2 = {'language': 'en', 'notifications_enabled': True, 'font_size': 12, 'theme': 'dark'}
    print(are_dicts_equal(sample_dict1, sample_dict2))