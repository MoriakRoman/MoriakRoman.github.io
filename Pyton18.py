def main():
#test


    FILENAME ='mbox.txt'


    mailfile = open(FILENAME, 'r')

    email_count = {}

    for line in mailfile:
        tokens = line.split()
        if len(tokens)> 1 and tokens[0] == 'From':
            if tokens[1] in email_count:
                email_count[tokens[1]] = email_count[tokens[1]] + 1
            else:
                email_count[tokens[1]] = 1
    print(email_count)

    email_count_list = [(v, k)for k, v in email_count.items()]

    email_count_list.sort(reverse = True)

    for key, val in email_count_list[0:10]:
        print(key, val)


if __name__ == '__main__':
    main()
