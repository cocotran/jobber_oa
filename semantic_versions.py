def increment(numbers: list, position: int) -> list:
    if position == -1:
        return numbers

    if position != 0 and numbers[position] == 9:
        numbers[position] = 0
        position -= 1
    else:
        numbers[position] += 1
        position = -1
    return increment(numbers, position)

def nextVersion(current_version: str) -> str:
    version_parts = [int(part) for part in current_version.split(".")]
    next_version = increment(version_parts, len(version_parts) - 1)
    return ".".join(str(part) for part in next_version)

assert(nextVersion("1.2.3") == "1.2.4")
assert(nextVersion("0.9.9") == "1.0.0")
assert(nextVersion("1") == "2")
assert(nextVersion("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9")
assert(nextVersion("9.9") == "10.0")
assert(nextVersion("9.9.9.9") == "10.0.0.0")
assert(nextVersion("9") == "10")