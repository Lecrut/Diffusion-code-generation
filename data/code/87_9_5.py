def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    sample_values = {
        'active': True,
        'inactive': False,
        'permission_yes': True,
        'permission_no': False
    }
    
    results = [
        can_proceed(sample_values['active'], sample_values['permission_yes']),
        can_proceed(sample_values['active'], sample_values['permission_no']),
        can_proceed(sample_values['inactive'], sample_values['permission_yes']),
        can_proceed(sample_values['inactive'], sample_values['permission_no'])
    ]
    
    for i, result in enumerate(results):
        print(f"Sample {i+1}: Active: {sample_values[f'active{i//2}']}, Permission: {sample_values[f'permission{i%2}']}, Result: {result}")