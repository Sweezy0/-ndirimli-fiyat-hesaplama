def indirim_yap(fiyat,yüzde):
    indirim_miktarı=fiyat*(yüzde/100)
    indirimli_fiyat=fiyat-indirim_miktarı
    print(f"İndirimli tutar:{indirimli_fiyat}")
indirim_yap(65,10)