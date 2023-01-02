from string import ascii_lowercase


def deduped(input: str, remainder: str = "") -> str:
    """Use recursion to remove duplicates characters from input string."""
    if input == "":
        return remainder
    if remainder == "":
        return deduped(input=input[1:], remainder=input[0])

    next = input[0]
    if next in remainder:
        return deduped(input[1:], remainder)

    return deduped(input[1:], remainder + next)


class AlphabetCipher(object):
    _key: str
    cipher: str

    def __init__(self, key: str):
        lower_cased = key.lower()
        letters = set(lower_cased)

        if len(lower_cased) > len(letters):
            print("You must use a key without repeating letters!")

        self._key = deduped(lower_cased)
        not_in_key = lambda c: c not in self._key
        remaining_letters = list(filter(not_in_key, ascii_lowercase))
        self.cipher = self._key + "".join(remaining_letters)

    def decode(self, encoded: str) -> str:
        input = encoded.lower()
        result = ""
        for c in input:
            index = self.cipher.index(c)
            result = result + ascii_lowercase[index]

        return result

    def encode(self, input: str) -> str:
        s = input.lower()
        result = ""
        for c in s:
            index = ascii_lowercase.index(c)
            result = result + self.cipher[index]

        return result

    def print_mapping(self):
        print(self.cipher)
        print(ascii_lowercase)

