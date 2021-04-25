'''
Lab 12 1

https://github.com/iamthewalrus67/palindromes
'''

from arraystack import ArrayStack


class Palindrome:
    '''
    Class for finding palindromes.
    '''
    @staticmethod
    def read_file(path):
        '''
        Return list of words from files.
        '''
        with open(path, 'r') as words:
            result = []
            for word in words:
                result.append(word.strip().split()[0])
            return result

    @staticmethod
    def write_to_file(palindromes, path):
        '''
        Write found palindromes to file.
        '''
        with open(path, 'w') as result_file:
            result_file.write('\n'.join(palindromes))

    @classmethod
    def find_palindromes(cls, input_path, output_path):
        '''
        Find palindromes in file and write them to another file.
        '''
        words = cls.read_file(input_path)
        palindromes = []

        for word in words:
            word_stack = ArrayStack()
            for char in word:
                word_stack.push(char)

            for i, _ in enumerate(word):
                if word[i] != word_stack.pop():
                    break

                if i == len(word)-1:
                    palindromes.append(word)

        cls.write_to_file(palindromes, output_path)
        return palindromes
