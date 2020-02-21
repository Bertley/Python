# function to return the index  
def getSubArray(arr, n, K, output = None, currentSum = 0, result = None): 
    if output == None: 
        currentSum = 0
        previousDifference = 0
        currentDifference = 0
        result = [-1, -1, abs(K-abs(currentSum))] 
        resultTmp = result 
        i = 0
        j = 0
        
        while(i <= j and j < n): 
            currentSum += arr[j] 
            previousDifference = currentDifference 
            currentDifference = K - abs(currentSum) 
            if(currentDifference <= 0): 
                if abs(currentDifference) < abs(previousDifference): 
                    resultTmp = [i, j, currentDifference] 
                else: 
                    resultTmp = [i, j-1, previousDifference] 
                currentSum -= (arr[i]+arr[j]) 
                i += 1
            else: 
                resultTmp = [i, j, currentDifference] 
                j += 1
            if(abs(resultTmp[2]) < abs(result[2])): 
                result = resultTmp 

        if currentSum == K: 
            print('-here')
            return [*range(result[0], result[1] + 1)]
        else:
            print('+here')
            return getSubArray(arr, n, K, [*range(result[0], result[1] + 1)], currentSum)
    else: 
        if currentSum == K:   
            print('here+')  
            return output
        else:
            print('here-')  
            print([*getSubArray(arr[:output[0]], len(arr[:output[0]]), K - (currentSum - arr[output[0]])), *output[1:]])
            return getSubArray(arr, n, K, [ *getSubArray(arr[:output[0]], len(arr[:output[0]]), K - (currentSum - arr[output[0]])), *output[1:]], currentSum)
    
  

# Driver Code 
def main(): 
    # arr = [7, 12, 12, 13, 14, 28, 29, 29, 30, 32, 32, 34, 41, 45, 46, 56, 61, 61, 62, 63, 65, 68, 76, 77, 77, 92, 93, 94, 97, 103, 113, 114, 114, 120, 135, 145, 145, 149, 156, 157, 160, 169, 172, 179, 184, 185, 189, 194, 195, 195]
    # arr = [2, 5, 6, 7]
    # arr = [4, 16, 17, 84, 95]
    arr = [476,650,1257,1824,2311,2740,2856,3024,3453,3768,5865,6233,6865,7591,8254,8542,9818,9904,10190,10695,12089,12912,13317,14389,14645,14886,15525,15633,16144,16598,18131,20375,20473,20531,21420,21804,22107,22445,23056,24864,25662,26041,26276,26291,26976,27083,27172,27875,28327,28469,28992,30145,30322,30404,30485,31295,32588,32989,33377,33710,34276,34356,35036,37693,37829,38530,38868,39070,40166,40656,41388,41723,41848,41883,42236,42264,43115,43911,45612,45818,46279,46593,47600,47777,48101,48276,48509,49456,51477,52629,52708,52778,53086,53096,53317,53923,54169,54666,54995,56264,56853,56888,57225,58706,58896,59693,59993,60789,61375,61534,61784,62586,63207,63542,63607,63969,65341,66338,66664,66696,67187,67399,68568,69454,70725,71313,71795,71900,71993,72002,72183,72357,72625,72843,72984,73252,73423,74350,74492,74688,74921,74929,76117,76416,76870,77500,77731,78514,78762,78949,79008,79097,79739,81298,82633,82678,82855,83718,84053,84267,84400,84542,85182,85935,86016,88076,88965,89369,89822,89865,90923,91212,92388,94562,94740,94820,95376,95725,95814,96177,96832,97302,97624,97787,97844,97974,98297,98958,101465,101690,101934,101964,102715,103249,103276,103882,104104,104231,104606,104888,105290,105440,105460,105958,106902,107226,107524,107621,107837,108669,109731,110716,111630,111815,111885,112286,113397,113400,113660,113719,114402,114627,115026,115317,116790,117021,117352,117359,119023,119220,119680,119997,120147,120167,120402,120815,120995,121086,121314,121603,121812,122394,123223,124256,125413,125761,126567,126933,126986,127304,127375,128144,129643,130445,130730,130940,131920,132091,132403,132429,132464,132782,132966,133521,133687,133878,134679,136357,137225,137286,137428,137846,138256,138630,138790,138941,139867,140865,142305,142342,143190,143474,145102,145146,146367,146464,146617,147042,147645,149196,149862,150120,151208,151719,151767,152691,154562,154772,154790,155338,155864,156277,156345,156496,158208,159148,159544,159835,160278,160314,160316,160473,161501,161910,162080,162111,162367,163049,163083,164187,164737,165131,165460,165700,165891,166122,166940,166982,167465,167804,168688,169447,169481,170446,170606,171390,171771,172588,172685,173112,173199,174033,174440,174497,175990,177985,178291,179502,182307,182531,182761,183024,183624,183751,184222,184481,184743,185703,187292,187381,188124,188209,188854,190356,190607,190723,192452,193370,194194,194902,196745,197867,199079,199173,199363,199418,199499,199710,199920,200388,200896,200947,201209,201680,201990,202562,203598,203931,206657,207479,208014,208547,208624,208853,208945,209095,209318,210599,210973,213497,213538,214232,215224,216932,217271,217932,219735,220332,220443,220912,221282,221326,221992,222137,222460,222474,223006,223559,224133,224181,224396,224694,225823,226492,226946,227874,228326,228603,229309,229522,229693,230025,230131,230334,230965,231199,231302,232171,232362,232411,233289,233803,234104,235164,235603,235663,235666,235780,236625,236701,238584,238587,238702,239019,240095,240113,240225,241343,241347,241787,242546,242771,243518,244013,244149,244367,244813,244958,245231,245935,246225,246256,246328,246680,247633,247912,248288,248779,249540,249616,250183,250331,250456,250918,250972,251134,251567,252048,252579,252623,253131,254697,254852,255174,255451,255621,255760,255887,256110,256201,256753,256787,256838,257471,258226,258658,259300,259346,259998,260273,260298,260786,261354,261701,261992,262297,262580,262852,262880,263370,263666,263677,264576,264710,264793,266365,267146,267780,268741,269503,270953,271833,272844,273483,273954,274731,274947,275555,276234,276858,277355,277363,277421,277456,277552,277797,277947,277983,278133,278136,278309,278412,278568,278586,279817,279837,279997,280079,280201,280797,281484,282653,283111,283252,284127,284964,285521,285628,285816,286244,286757,287687,287864,287987,288440,289333,289717,289739,289981,290171,290794,290833,291420,291527,291719,291755,291824,292055,292126,292187,292528,292734,293294,293379,295493,296502,296629,296796,297622,298202,298881,299156,299658,300147,300901,301389,301654,302071,302150,302269,302681,303496,305458,306090,306378,307470,307669,307808,308579,309496,309529,309622,310067,310295,310687,311171,311848,312993,313109,313169,313736,313972,314063,314620,314961,315619,316283,316848,316920,317001,317263,318645,318686,318913,319200,320066,320265,321131,321568,322502,322605,323283,323990,324359,325549,325896,326198,326909,327161,328889,328965,329215,329496,329846,330014,330827,330927,331586,331788,332094,332762,333683,335290,336704,337459,337953,338011,338029,339028,339549,339953,340086,340182,340853,342078,342640,342773,343305,343990,344258,344570,344576,345875,346290,346530,346910,347005,347286,348172,348372,348639,349550,349760,349810,351521,352212,352508,352788,352995,353945,354559,355058,355219,355835,356436,356750,356829,356922,357307,357857,359587,360506,360714,361939,362402,362530,364120,364914,366013,366694,367011,368254,368896,368951,369486,370909,371558,372111,372579,375241,375695,375927,376147,376446,376468,378462,379252,379404,379631,379676,379832,380354,380663,381964,382415,382605,382635,383593,383680,385229,386541,386865,386996,387202,387528,388213,388579,388622,389084,389569,391610,392128,393100,393588,395584,396973,397433,397450,397570,397593,397613,397938,398433,398519,398642,398906,398909,399585,399800,399940,400207,401175,401177,401625,401692,402270,402681,403431,403508,403957,404883,407575,407797,408447,408981,409437,413211,413792,414901,415062,415083,415973,416767,416842,417530,417872,418424,418852,419117,419144,419955,420223,420572,420702,421998,422111,422230,423440,423859,424007,424096,425851,426168,426207,426221,426884,427449,427860,427991,428180,428235,428282,428412,429944,430779,431122,431692,431763,432118,432373,433372,434623,435071,435088,435149,435724,435737,436021,436441,439426,439537,439640,439949,440514,440603,440920,441460,442093,442425,442468,442717,443194,443606,443743,444202,444205,444971,445841,445849,446224,447521,448513,449237,449296,449484,449711,450715,450821,451658,452040,452299,453065,454633,455103,455724,455935,456692,456783,457058,457109,457290,457643,459074,459432,459449,459520,460536,461290,461745,461916,462287,463238,463297,463349,463564,463689,463762,464122,464277,464707,464971,465281,466348,467625,468289,469996,470101,470456,471080,471983,472438,472449,472751,473468,474013,475486,475730,475814,475837,476137,476837,476856,476928,476970,477161,477514,477589,478685,479026,479078,479174,479485,480598,481192,481792,481945,482122,482713,483601,483914,484176,484468,484765,485151,486870,487166,487264,487333,487506,487626,487674,487904,488608,489761,490145,490836,491132,491516,492249,492347,492789,492892,493203,493406,493605,494430,495209,495682,495999,496002,496222,496300,496615,497783,498267,498420,499270,499431,499999,500200,500986,502019,504791,505305,505988,506731,507034,507770,507919,508187,508308,509044,509282,509283,509648,510362,511284,511701,511996,512313,512362,512391,513168,513476,514064,514714,514774,515662,515684,516605,517539,517832,518368,518443,519440,519587,520907,521892,522635,522758,523532,524834,524953,526220,526741,527327,528364,529349,529954,530010,530509,530589,531807,532374,532393,532452,532547,532980,533641,534201,534328,536055,536316,538220,539182,539644,540541,541773,542768,543169,543674,544224,545226,546673,547142,548008,548228,550172,551550,551691,553357,554685,554867,556167,556690,556762,556977,556983,557019,558633,558674,559594,560120,560132,560137,561945,562313,562326,562387,562687,563105,563709,563801,564366,564416,564658,564793,565209,565478,565543,565630,565661,565672,566262,566441,566483,566507,566898,567347,568583,569001,569020,569656,569878,570964,571066,571463,571909,572143,572712,573200,574536,574604,575949,576561,576869,577108,577175,577647,578094,578529,578778,578856,578907,579128,579415,580148,580150,580289,580409,580879,581179,581394,581593,582195,582816,582840,584055,584435,584533,585232,586126,587131,588204,588559,588688,588729,590231,590392,591415,591858,592053,592734,593469,593470,593474,594782,594967,596302,596801,596907,597398,597581,598833,599624,599755,602000,602784,603190,603685,603706,603817,604252,604289,604647,605101,605448,606845,607091,607365,607778,608144,608209,608843,609856,610856,611535,611929,612075,612502,612605,613006,613033,613813,614918,615499,615694,615921,616164,616937,617075,617164,617508,617940,618277,618490,618900,619227,620695,620910,621305,622554,622707,623449,623990,623999,624428,624885,624983,625135,625164,625431,625601,625831,626203,627137,628089,628543,629628,631313,632607,633090,633103,634261,635375,635707,635821,635914,636110,636181,636604,636796,638499,638602,638771,639149,639295,639768,640030,641018,641441,642463,645465,645609,645881,647504,648509,648615,649393,649519,649692,649864,650861,651102,651245,651383,651568,652534,652929,653476,653585,655471,655725,655839,655951,657244,657297,657762,657975,657988,658816,659227,660072,660407,660677,661810,661871,663737,664583,665097,665146,665671,665873,666320,666510,666614,667593,668112,668687,668905,668942,669618,670026,670038,670538,670607,671139,672148,672693,672926,674022,674130,676200,676907,677329,677619,677788,679049,679145,679163,679223,679565,680827,681454,681497,681504,681776,682105,683208,683465,683742,683874,685248,685794,686559,686638,686786,687328,687977,689356,689657,690254,690906,691044,691252,691849,692049,692145,692560,693220,693351,693435,693706,694073,694820,695014,695256,695663,695664,695979,696152,696263,696554,697280,699284,699338,699381,700056,700356,700697,701415,701525,702029,702309,702499,702736,702780,703106,703255,704365,704369,704989,705051,705528,705562,706124,707104,707166,707217,707668,708062,708497,709227,709621,710270,710301,710577,710738,712182,712577,713379,713587,713979,714876,714970,715249,716369,716802,717548,717695,717921,719038,719163,719847,720272,720826,720943,721075,721641,722182,722909,723429,723739,723862,723897,724207,724212,724637,725442,726404,727420,727710,727763,729359,729767,730231,730367,730480,731110,731127,731346,731431,732103,732219,733298,733493,733774,735183,735295,735394,735443,735962,737047,737186,737766,738134,738848,739536,739728,739996,740785,741347,741717,742276,742462,743266,744312,746471,747632,748257,749798,750851,751032,751464,752521,752838,753291,753303,753356,753680,754264,754428,754690,754768,755104,755782,755999,756372,757219,757588,758541,759410,759447,759833,761370,761945,763638,763985,764542,764595,765230,765439,766041,766587,767511,767985,769491,770265,770370,770814,771527,771762,772297,772394,772891,774534,776090,776697,777287,777623,777798,778042,778376,778531,779018,779289,779830,780892,780930,781228,781420,781937,782220,782595,782875,783092,783351,783841,783877,784307,784360,784526,785390,785446,785459,785935,786982,787403,787494,787676,788346,788438,788590,789410,790126,790221,790836,790921,791988,792003,792331,792546,793056,793239,795044,795718,796341,796958,797186,797356,797492,797600,798258,799026,799264,799601,799838,799980,800228,800632,801628,801960,802376,802835,803064,803086,804201,804802,805686,805870,805985,807240,807502,808628,810055,810126,810259,810671,810942,812035,812321,813268,813424,813474,813745,815502,815624,815860,816169,816283,816500,818062,819233,819539,820442,820703,821465,822208,822784,823318,823978,824680,824769,825064,825257,825673,826032,826148,826781,826969,827003,828409,828432,829141,829202,829734,830606,830935,831067,831182,831501,832342,834031,834743,834845,834867,834955,836638,836963,837353,837716,838192,838773,838793,839533,840397,840937,841255,843007,843221,843349,843722,843769,844202,844708,845013,845715,845738,845793,846015,846356,846386,846772,847323,847509,848800,850183,850206,850595,850874,852598,853136,853848,854647,855713,856304,856846,858230,859150,860445,860459,860667,861373,861773,862101,862327,862418,863925,864277,864329,864800,865049,865896,866836,869013,869685,869744,870178,870408,870864,870965,870968,871135,872115,872386,872616,873125,873345,873400,874241,874275,874295,874679,875187,875322,875518,876376,876617,876689,878208,879111,880046,880711,881385,882328,882605,883845,884693,886139,886416,886878,887255,888713,889259,889278,889596,889972,890895,891065,891648,892339,892748,893136,893191,893795,894192,894394,894838,894956,895967,896916,897055,897597,897645,898399,899449,900155,900351,901136,901413,901444,901973,902001,902288,902368,902563,902643,902982,903240,903393,903580,903616,903633,903733,905849,906048,906087,906390,906655,906702,906975,907139,907342,908587,908624,909010,910698,911578,911648,911894,911992,911997,912728,912855,913192,913290,913699,914584,914810,914863,915016,915163,916706,917015,917253,918449,918989,919086,919692,920710,920833,921457,922032,922091,922420,922910,923133,923486,923685,923704,924282,924508,925296,926055,927133,927238,927708,927818,928474,928514,928528,929232,930409,930597,932678,932982,933584,934778,934935,935004,935402,935569,936072,936457,940841,941474,941486,942624,942641,942701,943250,943364,943818,944326,945007,945037,945548,946330,946711,946846,947338,947359,947888,948126,948842,949365,949452,950957,951034,952185,952324,952589,952686,953613,953864,954718,954902,957010,957221,957327,957543,957851,957911,958500,959023,959766,960622,962088,963117,963161,964098,964260,964340,965549,965715,965991,966699,967147,967293,968165,968841,969446,970393,970586,970784,971417,971575,972786,974059,974087,974197,974281,975101,976082,977068,978008,978217,978464,978644,979073,979681,980073,980161,981008,981239,982204,984590,984719,984912,985988,986018,986093,986827,987254,987386,988261,988518,988587,988763,989035,990000,990103,991008,991158,991202,991391,991976,992068,992278,992893,992999,993116,993671,993846,994166,995018,995160,995281,995548,995791,996239,996780,997022,997118,997460,997793,998211,998294,999795,999867]
    n = len(arr)
    # K = 4500
    # K = 17
    K = 1000000000
    # K = 100
    
    
    pizzas = getSubArray(arr, n, K)

    sum = 0 
    for p in pizzas: 
        sum += arr[p]
    
    print(pizzas)
    print(sum)
    # if(i == -1):
    #     print("The empty array shows minimum Deviation")
    #     return 0 

    # result = []
    # for a in range(i, j+1):
    #     result.append(a)

    # return getClosest(arr, result, K)

main()
