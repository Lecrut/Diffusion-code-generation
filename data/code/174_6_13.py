def dictionaries_equal(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError('Both arguments must be dictionaries.')
    return set(dict1.items()) == set(dict2.items())
if __name__ == '__main__':
    sample_dict1 = {'theme': 'dark', 'font_size': 12, 'notifications_enabled': True, 'language': 'en'}
    sample_dict2 = {'language': 'en', 'font_size': 12, 'theme': 'dark', 'notifications_enabled': True}
    print(dictionaries_equal(sample_dict1, sample_dict2))