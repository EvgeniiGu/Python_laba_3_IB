#Такие инструкции настолько просты, что кажется лишнем тратить на них четыре строки. В некоторых случаях может появиться желание вложить такую конструкцию внутрь другой инструкции вместо того, чтобы выполнять присваивание переменной. По этим причинам и потому что в языке C имеется похожая позволяющая записать те же действия в виде единственного выражения, в языке Python была введено
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
encrypted_alphabet = {alphabet[i]: i for i in range(len(alphabet))}
deciphered_alphabet = {i: alphabet[i] for i in range(len(alphabet))}
text = input("text: ")
key = input("key: ")
iter = 0
chiper = []
for letter in text:
    if letter not in alphabet:
        chiper.append(letter)
        continue
    sum = encrypted_alphabet[key[iter]] + encrypted_alphabet[letter]
    sum -= len(alphabet) if sum > len(alphabet)-1 else 0
    chiper.append(sum)
    iter = 0 if iter == len(key)-1 else iter + 1
print(chiper)
iter = 0
decryption = ""
for element in chiper:
    if element not in list(deciphered_alphabet.keys()):
        decryption += element
        continue
    sum = element - encrypted_alphabet[key[iter]]
    sum += len(alphabet) if sum < 0 else 0
    decryption += str(deciphered_alphabet[sum])
    iter = 0 if iter == len(key)-1 else iter + 1
print(decryption)