def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    return len(text.split())

def char_count(text):
    dict = {}
    lowercase_str = text.lower()
    for ch in lowercase_str:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    return dict

def sort_on(dict):
    return dict["count"]

def report(text, path):
    dict = char_count(text)
    lst = []
    for key in dict:
        if key.isalpha():
            count_dict = {}
            count_dict["char"] = key
            count_dict["count"] = dict[key]
            lst.append(count_dict)
    lst.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count(text)} words found in the document")
    print()
    for d in lst:
        print(f"The '{d["char"]}' character was found {d["count"]} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    text = (read_file(path))
    # print(f"word count: {word_count(text)}")
    # print(char_count(text))
    report(text, path)

main()
