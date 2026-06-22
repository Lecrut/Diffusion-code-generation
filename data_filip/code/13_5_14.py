def snake_to_camel(s): return ''.join(w.capitalize() if i else w for i, w in enumerate(s.split('_')))
if __name__ == '__main__': print(snake_to_camel('my_variable_name'))