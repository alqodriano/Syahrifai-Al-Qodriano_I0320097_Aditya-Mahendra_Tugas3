# Nama, Hobi, Sosmed, Lagu favorit,dan  Makanan favorit
dict = {'Name'             : 'syahrifai al qodriano',
        'hobi'             : ['main game','tenis','renang'],
        'sosmed'           : {'IG' : 'alqodriano', 'facebook' : 'syahrifai al qodriano', 'twitter' : 'alqodriano'},
        'lagu favorit'     : ['hadal ahbek','ripped pants koplo','serta mulia'],
        'makanan favorit'  : ['tahu','tempe','ayam']}

print ('Nama     :', dict['Name'])
print ('facebook :', dict['sosmed'].get('facebook'))
print ('IG       :', dict['sosmed'].get('IG'))
print ('twiter   :', dict['sosmed'].get('twitter'))
print (*dict['lagu favorit'], sep= ",")
print (*dict['makanan favorit'], sep= ",")

# Mengubah salah satu hobi dan sosmed
dict['hobi'][1] = 'mukbang'
dict['sosmed']['facebook'] = 'alqodriano'

# Menghapus 2 makanan favorit
del dict['makanan favorit'][0]
del dict['makanan favorit'][1]


# Menambahkan 1 hobi
dict['hobi'].append('scroll tiktok')
print (*dict['hobi'], sep= ",")