def concatenate_parts(part1, part2):
    return part1 + part2

if __name__ == '__main__':
    greeting_parts = {
        "prefix": "Greetings from ",
        "suffix": "China!"
    }
    full_greeting = concatenate_parts(greeting_parts["prefix"], greeting_parts["suffix"])
    print(full_greeting)