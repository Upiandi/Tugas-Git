data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    },
}


print('===============================================================')
for i in data_panen.items():
    print(i)

print('===============================================================')
print(f'hasil panen jagung dari lokasi 2 : {data_panen["lokasi2"]['nama_lokasi']}: {data_panen['lokasi2']['hasil_panen']['jagung']}')

print('===============================================================')
print(f'nama lokasi ke-3 : {data_panen["lokasi3"]['nama_lokasi']}')

for id_lokasi, info in data_panen.items():
    nama = info['nama_lokasi']
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']

    print('===============================================================')
    print(f'nama lokasi : {nama} \njumlah panen padi : {padi} \njumlah panen jagung : {jagung}')

    if padi > 1300 or jagung > 800:
        print(f'{nama} memerlukan perhatian khusus')
    else:
        print(f'{nama} dalam kondisi baik')
print('===============================================================')