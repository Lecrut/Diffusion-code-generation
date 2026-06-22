from enum import IntFlag, auto

class Permissions(IntFlag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()

def check_access(user_flags, required_flags):
    if not isinstance(user_flags, IntFlag):
        raise ValueError("user_flags must be an IntFlag instance")
    if not isinstance(required_flags, IntFlag):
        raise ValueError("required_flags must be an IntFlag instance")
    
    if required_flags == 0:
        return True
    
    current = user_flags
    result = True
    
    if required_flags & Permissions.READ:
        if not (current & Permissions.READ):
            return False
        current &= ~Permissions.READ
        result = current == 0 or (current & (required_flags & ~Permissions.READ)) == 0
    
    if required_flags & Permissions.WRITE:
        if not (current & Permissions.WRITE):
            return False
        current &= ~Permissions.WRITE
        if not result:
            return False
        result = current == 0 or (current & (required_flags & ~Permissions.WRITE)) == 0
        
    if required_flags & Permissions.EXECUTE:
        if not (current & Permissions.EXECUTE):
            return False
        current &= ~Permissions.EXECUTE
        if not result:
            return False
        result = current == 0 or (current & (required_flags & ~Permissions.EXECUTE)) == 0
        
    if required_flags & Permissions.DELETE:
        if not (current & Permissions.DELETE):
            return False
        current &= ~Permissions.DELETE
        if not result:
            return False
        result = current == 0 or (current & (required_flags & ~Permissions.DELETE)) == 0
        
    return result

if __name__ == '__main__':
    user_perms = Permissions.READ | Permissions.WRITE
    required = Permissions.READ | Permissions.EXECUTE
    access_granted = check_access(user_perms, required)
    print(access_granted)
    
    user_perms_full = Permissions.READ | Permissions.WRITE | Permissions.EXECUTE
    required_full = Permissions.READ | Permissions.EXECUTE
    full_access = check_access(user_perms_full, required_full)
    print(full_access)
    
    user_perms_write = Permissions.WRITE
    required_write = Permissions.WRITE | Permissions.DELETE
    write_only = check_access(user_perms_write, required_write)
    print(write_only)