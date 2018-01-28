
def count_letters(word, char):
    count = 0
    while count <= len(word):
        for char in word:
            if char == word[count]:
                count += 1
            return count

print 'Keneau the Kat'.count('K')
print 'banana'.count('a')
