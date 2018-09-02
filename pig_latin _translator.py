#get sentence from user

original = input("Enter your sentence here: ").strip().lower()

#split sentence into words

words = original.split()

new_words = []

#loop through words and convert to pig latin

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position +1
            else:
                break
        new_word = word[vowel_position:] + word[:vowel_position] + "ay"
        new_words.append(new_word)
       
#stick words back together

pig_latin = " ".join(new_words)

#output the final string

print(pig_latin)
