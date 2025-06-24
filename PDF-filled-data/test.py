from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pdfrw import PdfReader, PdfWriter, PageMerge
import json
"""
PDF Size horizontal to vertical = 840 by 590
"""
with open('visa_application.json', 'r') as file:
    form_data = json.load(file)

overlay_pdf_path = "overlay.pdf"
c = canvas.Canvas(overlay_pdf_path, pagesize=A4)
check = "✔"

def draw_text_in_boxes(start_x, start_y, text):
    for i, char in enumerate(text):
        char_x = start_x + i * 17
        c.drawString(char_x + 3, start_y, char)
name = form_data[0]['FullName'].strip().upper() + " " + form_data[0]['MiddleName'].strip().upper()
if name is not None and name != "":
    draw_text_in_boxes(141, 650, name)
surname = form_data[0]['Surname']
if surname is not None and surname != "":
    draw_text_in_boxes(141, 628, surname[:25].upper())

alias = form_data[0]['Alias']
if alias is not None and alias != "":
    draw_text_in_boxes(141, 599, alias[:25].upper())
    draw_text_in_boxes(141, 579, alias[25:50].upper())


dob = form_data[0]['DateOfBirth']
if dob is not None and dob != "":
    draw_text_in_boxes(115, 546, dob.split("-")[0])
    draw_text_in_boxes(161, 546, dob.split("-")[1])
    draw_text_in_boxes(210, 546, dob.split("-")[2])

male = form_data[0]['GenderM']
if male is True and male != "":
    draw_text_in_boxes(346, 543, check)

female = form_data[0]['GenderF']
if female is True and female != "":
    draw_text_in_boxes(397, 543, check)

MSSingle = form_data[0]['MSSingle']
if MSSingle is True and MSSingle != "":
    draw_text_in_boxes(104, 507, check)
MSMarried = form_data[0]['MSMarried']
if MSMarried is True and MSMarried != "":
    draw_text_in_boxes(156, 507, check)
# MSSeparated = form_data[0]['MSSeparated']
# if MSSeparated is True and MSSeparated != "":
#     draw_text_in_boxes(212, 507, check)
MSDivorced = form_data[0]['MSDivorced']
if MSDivorced is True and MSDivorced != "":
    draw_text_in_boxes(276, 507, check)
MSWidowed = form_data[0]['MSWidowed']
if MSWidowed is True and MSWidowed != "":
    draw_text_in_boxes(334, 507, check)
MSCohabited = form_data[0]['MSCohabited']
if MSCohabited is True and MSCohabited != "":
    draw_text_in_boxes(397, 507, check)
MSCustomary = form_data[0]['MSCustomary']
if MSCustomary is True and MSCustomary != "":
    draw_text_in_boxes(464, 507, check)

SpouseCitizen = form_data[0]['SpouseCitizen']
if SpouseCitizen is True and SpouseCitizen != "":
    NRICNo1 = form_data[0]['NRICNo1']
    draw_text_in_boxes(159, 475, check)
    draw_text_in_boxes(372, 475, NRICNo1)
SpousePR = form_data[0]['SpousePR']
if SpousePR is True and SpousePR != "":
    NRICNo2 = form_data[0]['NRICNo2']
    draw_text_in_boxes(159, 455, check)
    draw_text_in_boxes(372, 450, NRICNo2)
SpouseOthers = form_data[0]['SpouseOthers']
if SpouseOthers is not None and SpouseOthers != "":
    draw_text_in_boxes(159, 432, check)
    c.setFont("Helvetica", 10)
    c.drawString(286, 428, SpouseOthers)
    c.setFont("Helvetica", 12)

CountryOfBirth = form_data[0]['CountryOfBirth']
if CountryOfBirth is not None and CountryOfBirth != "":
    draw_text_in_boxes(143, 398, CountryOfBirth.upper())
StateOfBirth = form_data[0]['StateOfBirth']
if StateOfBirth is not None and StateOfBirth != "":
    draw_text_in_boxes(143, 373, StateOfBirth.upper())
RaceName = form_data[0]['RaceName']
if RaceName is not None and RaceName != "":
    draw_text_in_boxes(143, 346, RaceName.upper())
NationalityName = form_data[0]['NationalityName']
if NationalityName is not None and NationalityName != "":
    draw_text_in_boxes(143, 321, NationalityName.upper())

InternationalPassport = form_data[0]['InternationalPassport']
if InternationalPassport is True and InternationalPassport != "":
    c.drawString(199, 274, check)
DiplomaticPassport = form_data[0]['DiplomaticPassport']
if DiplomaticPassport is True and DiplomaticPassport != "":
    c.drawString(318, 274, check)
OfficialPassport = form_data[0]['OfficialPassport']
if OfficialPassport is True and OfficialPassport != "":
    c.drawString(428, 274, check)
ServicePassport = form_data[0]['ServicePassport']
if ServicePassport is True and ServicePassport != "":
    c.drawString(199, 261, check)
DocOfIdentity = form_data[0]['DocOfIdentity']
if DocOfIdentity is True and DocOfIdentity != "":
    c.drawString(318, 261, check)
CertOfIdentity = form_data[0]['CertOfIdentity']
if CertOfIdentity is True and CertOfIdentity != "":
    c.drawString(428, 261, check)
TypeOfTravelOthers = form_data[0]['TypeOfTravelOthers']
if TypeOfTravelOthers is not None and TypeOfTravelOthers != "":
    c.drawString(199, 248, check)
    c.setFont("Helvetica", 10)
    c.drawString(314, 247, TypeOfTravelOthers)
    c.setFont("Helvetica", 12)
PassportNo = form_data[0]['PassportNo']
if PassportNo is not None and PassportNo != "":
    draw_text_in_boxes(142, 218, PassportNo)
IssueDate = form_data[0]['IssueDate']
if IssueDate is not None and IssueDate != "":
    draw_text_in_boxes(142, 186, IssueDate.split("-")[0])
    draw_text_in_boxes(190, 186, IssueDate.split("-")[1])
    draw_text_in_boxes(240, 186, IssueDate.split("-")[2])
ExpiryDate = form_data[0]['ExpiryDate']
if ExpiryDate is not None and ExpiryDate != "":
    draw_text_in_boxes(397, 186, ExpiryDate.split("-")[0])
    draw_text_in_boxes(446, 186, ExpiryDate.split("-")[1])
    draw_text_in_boxes(496, 186, ExpiryDate.split("-")[2])
PassportOfIssue = form_data[0]['PassportOfIssue']
if PassportOfIssue is not None and PassportOfIssue != "":
    draw_text_in_boxes(141, 145, PassportOfIssue.upper())

PRCIDNo = form_data[0]['PRCIDNo']
if PRCIDNo is not None and PRCIDNo != "":
    draw_text_in_boxes(141, 94, PRCIDNo[:18])

c.showPage()

CountryOfResidence = form_data[0]['CountryOfResidence']
if CountryOfResidence is not None and CountryOfResidence != "":
    draw_text_in_boxes(141, 757, CountryOfResidence[:25].upper())

DivisonOfResidence = form_data[0]['DivisonOfResidence']
if DivisonOfResidence is not None and DivisonOfResidence != "":
    draw_text_in_boxes(141, 723, DivisonOfResidence[:25].upper())

PerfectureofResidence = form_data[0]['PerfectureofResidence']
if PerfectureofResidence is not None and PerfectureofResidence != "":
    draw_text_in_boxes(141, 689, PerfectureofResidence[:25].upper())

DistrictofResidence = form_data[0]['DistrictofResidence']
if DistrictofResidence is not None and DistrictofResidence != "":
    draw_text_in_boxes(141, 659, DistrictofResidence[:25].upper())

CountryAddressData = form_data[0]['CountryAddressData']
if CountryAddressData is not None and CountryAddressData != "":
    c.setFont("Helvetica", 8)
    c.drawString(75, 623, CountryAddressData.upper())
    c.setFont("Helvetica", 12)


ApplicantEmailID = form_data[0]['ApplicantEmailID']
if ApplicantEmailID is not None and ApplicantEmailID != "":
    draw_text_in_boxes(141, 568, ApplicantEmailID.upper())
ApplicantContactNo = form_data[0]['ApplicantContactNo']
if ApplicantContactNo is not None and ApplicantContactNo != "":
    draw_text_in_boxes(141, 540, ApplicantContactNo)
Occupation = form_data[0]['Occupation']
if Occupation is not None and Occupation != "":
    draw_text_in_boxes(141, 514, Occupation.upper())

QualNoFormalEducation = form_data[0]['QualNoFormalEducation']
if QualNoFormalEducation is True and QualNoFormalEducation != "":
    c.drawString(144,487, check)
QualPrimary = form_data[0]['QualPrimary']
if QualPrimary is True and QualPrimary != "":
    c.drawString(260,487, check)
QualSecondary = form_data[0]['QualSecondary']
if QualSecondary is True and QualSecondary != "":
    c.drawString(320,487, check)
QualPreUniversity = form_data[0]['QualPreUniversity']
if QualPreUniversity is True and QualPreUniversity != "":
    c.drawString(392,487, check)
QualDiploma =  form_data[0]['QualDiploma']
if QualDiploma is True and QualDiploma !=  "":
    c.drawString(144,467, check)
QualUniversity =  form_data[0]['QualUniversity']
if QualUniversity is True and QualUniversity != "":
    c.drawString(210,467, check)
QualPG =  form_data[0]['QualPG']
if QualPG is True and QualPG != "":
    c.drawString(290,467, check)

AnnualIncome = form_data[0]['AnnualIncome']
if AnnualIncome is not None and AnnualIncome != "":
    draw_text_in_boxes(145, 430, AnnualIncome)
Religion = form_data[0]['Religion']
if Religion is not None and Religion != "":
    draw_text_in_boxes(143, 400, Religion.upper())

ArrivalDate = form_data[0]['ArrivalDate']
if ArrivalDate is not None and ArrivalDate != "":
    draw_text_in_boxes(203, 373, ArrivalDate.split("-")[0])
    draw_text_in_boxes(252, 373, ArrivalDate.split("-")[1])
    draw_text_in_boxes(300, 373, ArrivalDate.split("-")[2])

VisaSingle = form_data[0]['VisaSingle']
if VisaSingle is True and VisaSingle != "":
    c.drawString(98, 329, check)
VisaDouble = form_data[0]['VisaDouble']
if VisaDouble is True and VisaDouble != "":
    c.drawString(187, 329, check)
VisaTriple = form_data[0]['VisaTriple']
if VisaTriple is True and VisaTriple != "":
    c.drawString(276, 329, check)
VisaMultiple = form_data[0]['VisaMultiple']
if VisaMultiple is True and VisaMultiple != "":
    c.drawString(367, 329, check)

PurposeBusiness = form_data[0]['PurposeBusiness']
if PurposeBusiness is True and PurposeBusiness != "":
    draw_text_in_boxes(209, 307, check)
PurposeSocial = form_data[0]['PurposeSocial']
if PurposeSocial is True and PurposeSocial != "":
    draw_text_in_boxes(138, 307, check)
PurposeDetails = form_data[0]['PurposeDetails']
if PurposeDetails is not None and PurposeDetails != "":
    c.setFontSize(10)
    c.drawString(125, 277, PurposeDetails[:100])

StayUnder30 = form_data[0]['StayUnder30']
if StayUnder30 is True and StayUnder30 != "":
    draw_text_in_boxes(240, 245, check)
StayOver30 = form_data[0]['StayOver30']
if StayOver30 is True and StayOver30 != "":
    draw_text_in_boxes(352, 245, check)
LongStayInfo = form_data[0]['LongStayInfo']
if LongStayInfo is not None and LongStayInfo != "":
    c.setFontSize(8)
    c.drawString(35, 190, LongStayInfo[:110].upper())
    c.drawString(35, 172, LongStayInfo[110:210].upper())
    c.drawString(35, 154, LongStayInfo[210:260].upper())
    # c.drawString(35, 136, LongStayInfo[450:600].upper())

c.showPage()

AccNextOfKin = form_data[0]['AccNextOfKin']
if AccNextOfKin is True and AccNextOfKin != "":
    c.drawString(25, 745, check)
AccRelative = form_data[0]['AccRelative']
if AccRelative is True and AccRelative != "":
    c.drawString(123, 745, check)
AccFriend = form_data[0]['AccFriend']
if AccFriend is True and AccFriend != "":
    c.drawString(215, 745, check)
AccHotel = form_data[0]['AccHotel']
if AccHotel is True and AccHotel != "":
    c.drawString(303, 745, check)
AccOthers = form_data[0]['AccOthers']
if AccOthers is not None and AccOthers != "":
    c.drawString(350, 745, check)
    c.setFont("Helvetica", 8)
    c.drawString(470, 742, AccOthers)
    c.setFont("Helvetica", 12)


HouseNo = form_data[0]['HouseNo']
if HouseNo is not None and HouseNo != "":
    draw_text_in_boxes(32, 700, HouseNo)
FloorNo = form_data[0]['FloorNo']
if FloorNo is not None and FloorNo != "":
    draw_text_in_boxes(161, 700, FloorNo)
Unitname = form_data[0]['Unitname']
if Unitname is not None and Unitname != "":
    draw_text_in_boxes(247, 700, Unitname)
PostalCode = form_data[0]['PostalCode']
if PostalCode is not None and PostalCode != "":
    draw_text_in_boxes(363, 700, PostalCode)
StreetName = form_data[0]['StreetName']
if StreetName is not None and StreetName != "":
    draw_text_in_boxes(99, 675, StreetName)
ContactNo = form_data[0]['ContactNo']
if ContactNo is not None and ContactNo != "":
    c.drawString(500, 677, ContactNo)
BuildingName = form_data[0]['BuildingName']
if BuildingName is not None and BuildingName != "":
    c.setFont("Helvetica", 8)
    c.drawString(99, 647, BuildingName[:100].upper())
    c.setFont("Helvetica", 12)
ResidedYes = form_data[0]['ResidedYes']
if ResidedYes is True and ResidedYes != "":
    c.drawString(60, 590, check)
    # ResidenceDetails
    c.setFont("Helvetica", 10)
    CountryPlace = form_data[0]['ResidenceDetails'][0]['CountryPlace']
    if CountryPlace is not None and CountryPlace != "":
        c.drawString(60, 520, CountryPlace)
    Address = form_data[0]['ResidenceDetails'][0]['Address']
    if Address is not None and Address != "":
        c.drawString(216, 520, Address[:30].upper())
        c.drawString(216, 508, Address[30:60].upper())
    From = form_data[0]['ResidenceDetails'][0]['From']
    if From is not None and From != "":
        c.drawString(475, 520, From)
    To = form_data[0]['ResidenceDetails'][0]['To']
    if To is not None and To != "":
        c.drawString(539, 520, To)
    c.setFont("Helvetica", 12)
ResidedNo = form_data[0]['ResidedNo']

if ResidedNo is True and ResidedNo != "":
    c.drawString(112, 590, check)

RelToApplicant  = form_data[0]['RelToApplicant']
if RelToApplicant is not None and RelToApplicant != "":
    draw_text_in_boxes(140, 347, RelToApplicant[:25].upper())
name = form_data[0]['Name']
if name is not None and name != "":
    draw_text_in_boxes(140, 289, name[:25].upper())
    draw_text_in_boxes(140, 270, name[25:50].upper())

CompanionDOB = form_data[0]['CompanionDOB']
if CompanionDOB is not None and CompanionDOB != "":
    draw_text_in_boxes(143, 236, CompanionDOB.split("-")[0])
    draw_text_in_boxes(192, 236, CompanionDOB.split("-")[1])
    draw_text_in_boxes(240, 236, CompanionDOB.split("-")[2])
GenderMale = form_data[0]['GenderMale']
if GenderMale is True and GenderMale != "":
    c.drawString(375, 234, check)
GenderFemale = form_data[0]['GenderFemale']
if GenderFemale is True and GenderFemale != "":
    c.drawString(427, 234, check)

Nationality = form_data[0]['Nationality']
if Nationality is not None and Nationality != "":
    draw_text_in_boxes(141, 193, Nationality[:25].upper())
TravelDocNo = form_data[0]['TravelDocNo']
if TravelDocNo is not None and TravelDocNo != "":
    draw_text_in_boxes(141, 165, TravelDocNo[:15].upper())

c.showPage()

LocContactName = form_data[0]['LocContactName']
if LocContactName is not None and LocContactName != "":
    draw_text_in_boxes(141, 753, LocContactName[:25].upper())
    draw_text_in_boxes(141, 735, LocContactName[25:50].upper())
LocContactRelation = form_data[0]['LocContactRelation']
if LocContactRelation is not None and LocContactRelation != "":
    draw_text_in_boxes(141, 695, LocContactRelation[:25].upper())
LocContactNo = form_data[0]['LocContactNo']
if LocContactNo is not None and LocContactNo != "":
    c.drawString(98, 650, LocContactNo)

LocContactEmail = form_data[0]['LocContactEmail']
if LocContactEmail is not None and LocContactEmail != "":
    # c.setFont("Helvetica", 10)
    c.drawString(330, 650, LocContactEmail)
    c.setFont("Helvetica", 12)

details = False
AntRefusedEntry = form_data[0]['AntRefusedEntry']
if AntRefusedEntry is True and AntRefusedEntry != "":
    c.drawString(470, 581, check)
    details = True
else:
    c.drawString(516, 581, check)

AntConvicted = form_data[0]['AntConvicted']
if AntConvicted is True and AntConvicted != "":
    c.drawString(470, 562, check)
    details = True
else:
    c.drawString(516, 562, check)
AntProhibitedSG = form_data[0]['AntProhibitedSG']
if AntProhibitedSG is True and AntProhibitedSG != "":
    c.drawString(470, 544, check)
    details = True
else:
    c.drawString(516, 544, check)

AntDiffPassport = form_data[0]['AntDiffPassport']
if AntDiffPassport is True and AntDiffPassport != "":
    c.drawString(470, 527, check)
    details = True
else:
    c.drawString(516, 527, check)

AntDetails = form_data[0]['AntDetails']
if details:
    if AntDetails is not None and AntDetails != "":
        c.setFontSize(8)
        c.drawString(35, 484, AntDetails[:110].upper())
        c.drawString(35, 469, AntDetails[110:220].upper())
        c.drawString(35, 453, AntDetails[220:330].upper())
        c.setFont("Helvetica", 12)

DeclarationDate = form_data[0]['DeclarationDate']
if DeclarationDate is not None and DeclarationDate != "":
    c.drawString(94, 57, DeclarationDate)

cross_sign = "x"
Signature = form_data[0]['Signature']
if Signature is  None or Signature != "":
    c.drawString(312, 62, cross_sign)



c.save()

template_pdf_path = "Asingapore form.pdf"
output_pdf_path = "Filled_Form.pdf"

template_pdf = PdfReader(template_pdf_path)
overlay_pdf = PdfReader(overlay_pdf_path)

for page, overlay in zip(template_pdf.pages, overlay_pdf.pages):
    merger = PageMerge(page)
    merger.add(overlay).render()

PdfWriter(output_pdf_path, trailer=template_pdf).write()
print("Filled PDF saved as:", output_pdf_path)
