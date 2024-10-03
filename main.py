
def countWords(string: str) -> int:
    words: list = string.split()
    return len(words)

def countCharacters(string: str) -> dict:
    char_dict = {}
    lowered_string: str = string.lower()

    for char in lowered_string:
        if not char.isalpha():
            continue
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    return char_dict

def report(document_name: str, document_contents: str) -> None:
    total_words: int = countWords(document_contents)
    total_chars_dict: dict = countCharacters(document_contents)

    print(f"-- Begin report of {document_name} --")
    print(f"{total_words} words found in the document \n")

    for char in total_chars_dict.keys():
        print(f"The '{char}' character was found {total_chars_dict[char]} times")

    print("-- End report --")


def main():
    document_name: str = "books/frankenstein.txt"
    with open(document_name) as f:
        file_content = f.read()
    
    report(document_name, file_content)


main()