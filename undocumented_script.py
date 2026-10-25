
def process_numbers(numbers):
    """
    Process a list of numbers based on whether they are even or odd.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: Even numbers doubled and odd numbers tripled.
    """
    # Double even numbers and triple odd numbers.
    return [num * 2 if num % 2 == 0 else num * 3 for num in numbers]


def process_strings(strings):
    """
    Process a list of strings based on their length.

    Args:
        strings (list): A list of words.

    Returns:
        str: Words longer than five characters in uppercase,
        and shorter words in lowercase.
    """
    # Change word capitalization based on length.
    processed_words = [
        word.upper() if len(word) > 5 else word.lower()
        for word in strings
    ]

    return " ".join(processed_words)


def main():
    """
    Run the program and display the processed results.

    Returns:
        None
    """
    numbers = [1, 2, 3, 4, 5, 6, 7]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(words)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
