from hashlib import sha256

def SHA256(text):
    return (sha256(text.encode("ascii")).hexdigest())

def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str = '0'* prefix_zeros
    for nonce in range(10000000):
        text=str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if(new_hash.startswith(prefix_str)):
            print(f'Mining successful with nonce : {nonce}')
            return new_hash
    raise BaseException('No luck dude')

if __name__=='__main__':
    transactions='''
    A->B->10,
    C->d->34
    '''
    #print(SHA256("ABC"))
    difficulty = 6
    new_hash = mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',difficulty)
    print(new_hash)

    #print(SHA256(transactions))